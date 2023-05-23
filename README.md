# EQT Test

This repository contains code to solve an assigned EQT code test.

## Possible improvements
- UUID is likely better for merging *.json's than company name.
  - If not, at least some similarity metric for company names. Right now they have to match perfectly.
- Nicer to have abstraction layer for read/transform/write, so interface is equivalent. I.e if main can be changed to
```python
dfs = read(urls)

transformed_dfs = []
for df in dfs:
    transformed_dfs.append(transform_df(df))

merged_df = merge(dfs)

write(merged_df)
```
- "Equivalent" of Scala datasets (Pydantic classes?), giving schemas to each dataset and its' transformed output
  - This will allow to unit test everything more effectively if data mocks are set up and easily available.
- Config or argparser for paths, URLs etc.