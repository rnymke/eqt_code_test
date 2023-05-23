import pandas as pd
import datetime as dt
from eqt.transformer.transformer import rename_divestments


def test_rename_divestments():
    input_df = pd.DataFrame(data={"entry": [dt.datetime.now(), dt.datetime.now()],
                                  "exit": [dt.datetime.now(), dt.datetime.now()],
                                  "funds": [dt.datetime.now(), dt.datetime.now()],
                                  "dummy": ["a", "b"]
                                  }
                            )
    output_df = rename_divestments(input_df)

    # Check that columns are renamed properly
    assert list(output_df.columns) == ["previous_entry", "previous_exit", "previous_funds", "dummy"]

    # Check that num rows is unchanged
    assert len(output_df) == 2

    # TODO: assert DF is equal except for column changes