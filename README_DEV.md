# Dev Readme

## Steps
1. Install Python 3.11.9 (which is the MLHub version)
2. Acquire all custom MLHub packages as zip files and place them in a `_sdk` folder. There should be 8 files.
3. Install mlhub_requirements.txt
4. Install dev_requirements.txt
5. Configure your authentication by modifying `run_jupyter.py`.
6. Run `run_jupyter.py` to start notebooks. The token will automatically be set and updated.
7. If you created a new public notebook example, include its description in `README.md` 
8. Commit and push the notebook and `README.md` to GitHub on the dev branch.  
9. Transfer the updates to the main branch by switching to main and then selectively checking them out:
    ```bash
    git checkout -p dev -- "<notebook path>.ipynb"
    git checkout -p dev -- "README.md"
    ```

## Notes
- Using the SDK to load local TrendHub and ContextHub views does not work, since these use local urls
- The requirement `lightgbm==4.0.0` does not install locally, and has been left out of `mlhub_requirementx.txt`
