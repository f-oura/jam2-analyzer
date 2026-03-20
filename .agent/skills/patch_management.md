# Skill: Submodule Patch Management

This skill describes how to handle custom modifications to external submodules in `jam2-analyzer`.

## When to use
Use this when you need to fix a bug or add a feature to the JAM2 source code in `jam2-code/`.

## Procedure
1.  **Modify Source**: Edit files directly within the `jam2-code/` directory.
2.  **Verify**: Build and test the changes locally using `./setup.sh`.
3.  **Stage Changes**: Use `git -C jam2-code add <modified_file>` to stage ONLY the relevant source code changes.
4.  **Update Patch**: Update the official compatibility patch by running:
    ```bash
    git -C jam2-code diff --cached > patches/jam2_compatibility.patch
    ```
5.  **Commit Patch**: Commit the updated `patches/jam2_compatibility.patch` in the main `jam2-analyzer` repository.
6.  **Maintain Clean Submodule**: Optionally, avoid committed local changes in `jam2-code` to keep the working tree clean for others.
