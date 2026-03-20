#!/usr/bin/env python3
import sys
import os
import gzip
import array

try:
    import ROOT
except ImportError:
    print("Error: PyROOT is not installed or not in PYTHONPATH.")
    sys.exit(1)

def parse_phase_dat(filename, out_root_name):
    """
    Parses JAM2 phase.dat.gz and converts it to a ROOT TTree.
    """
    # Create output directory if it doesn't exist
    out_dir = os.path.dirname(out_root_name)
    if out_dir and not os.path.exists(out_dir):
        print(f"Creating directory: {out_dir}")
        os.makedirs(out_dir)

    print(f"Opening {filename} and writing to {out_root_name}...")
    
    f_out = ROOT.TFile(out_root_name, "RECREATE")
    tree = ROOT.TTree("tree", "JAM2 Phase Space Data")

    # Variables for TTree (Event level)
    iev = array.array('i', [0])
    nv = array.array('i', [0])
    b = array.array('d', [0.0])
    npart = array.array('i', [0])
    ncoll = array.array('i', [0])

    # Particle variables (using std::vector for variable multiplicity)
    status = ROOT.std.vector('int')()
    pid = ROOT.std.vector('int')()
    p_ncoll = ROOT.std.vector('int')()
    mass = ROOT.std.vector('double')()
    px = ROOT.std.vector('double')()
    py = ROOT.std.vector('double')()
    pz = ROOT.std.vector('double')()
    energy = ROOT.std.vector('double')()
    vx = ROOT.std.vector('double')()
    vy = ROOT.std.vector('double')()
    vz = ROOT.std.vector('double')()
    vt = ROOT.std.vector('double')()
    vtf = ROOT.std.vector('double')()

    tree.Branch("iev", iev, "iev/I")
    tree.Branch("nv", nv, "nv/I")
    tree.Branch("b", b, "b/D")
    tree.Branch("npart", npart, "npart/I")
    tree.Branch("ncoll", ncoll, "ncoll/I")

    tree.Branch("status", status)
    tree.Branch("pid", pid)
    tree.Branch("p_ncoll", p_ncoll)
    tree.Branch("mass", mass)
    tree.Branch("px", px)
    tree.Branch("py", py)
    tree.Branch("pz", pz)
    tree.Branch("energy", energy)
    tree.Branch("x", vx)
    tree.Branch("y", vy)
    tree.Branch("z", vz)
    tree.Branch("t", vt)
    tree.Branch("tf", vtf)

    try:
        opener = gzip.open if filename.endswith(".gz") else open
        with opener(filename, 'rt') as f:
            # First line is a global header
            f.readline()
            
            event_count = 0
            for line in f:
                if line.startswith("#"):
                    # Fill data from previous event if any exists
                    if status.size() > 0:
                        tree.Fill()
                        event_count += 1
                    
                    # Clear vectors for next event
                    status.clear(); pid.clear(); p_ncoll.clear(); mass.clear()
                    px.clear(); py.clear(); pz.clear(); energy.clear()
                    vx.clear(); vy.clear(); vz.clear(); vt.clear(); vtf.clear()

                    # Parse event header: # iev nv ncollG npartG b npart ncoll ncollBB
                    parts = line.strip().split()
                    if len(parts) >= 8:
                        iev[0] = int(parts[1])
                        nv[0] = int(parts[2])
                        b[0] = float(parts[5])
                        npart[0] = int(parts[6])
                        ncoll[0] = int(parts[7])
                else:
                    # Parse particle data: status pid ncoll mass px py pz energy x y z time tf
                    parts = line.strip().split()
                    if len(parts) >= 13:
                        status.push_back(int(parts[0]))
                        pid.push_back(int(parts[1]))
                        p_ncoll.push_back(int(parts[2]))
                        mass.push_back(float(parts[3]))
                        px.push_back(float(parts[4]))
                        py.push_back(float(parts[5]))
                        pz.push_back(float(parts[6]))
                        energy.push_back(float(parts[7]))
                        vx.push_back(float(parts[8]))
                        vy.push_back(float(parts[9]))
                        vz.push_back(float(parts[10]))
                        vt.push_back(float(parts[11]))
                        vtf.push_back(float(parts[12]))

            # Fill final event
            if status.size() > 0:
                tree.Fill()
                event_count += 1
                
        print(f"Extraction complete! Total events: {event_count}")
        tree.Write()
        f_out.Close()
        
    except Exception as e:
        print(f"Error during parsing: {e}")
        f_out.Close()
        sys.exit(1)

if __name__ == "__main__":
    inf = "phase.dat.gz" if len(sys.argv) < 2 else sys.argv[1]
    outf = "rootfile/phase.root" if len(sys.argv) < 3 else sys.argv[2]
    
    # Check if input file exists
    if not os.path.exists(inf):
        print(f"Error: Input file '{inf}' not found.")
        sys.exit(1)
        
    parse_phase_dat(inf, outf)
