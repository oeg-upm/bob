from Detection import get_num_kind
# import pandas as pd
#
# CATEGORICAL = 'categorical'
# UNKNOWN = 'unknown'
#
#
# def detect_column_types(file_dir):
#     """
#     :param file_dir: the location of the data file
#     :return: the list of types
#     """
#     from categorical import is_categorical
#
#     funcs_and_types = {
#         CATEGORICAL: is_categorical,
#     }
#
#     ext = file_dir[-4:]
#     if ext == ".csv":
#         df = pd.read_csv(file_dir)
#     else:
#         df = None
#
#     types = []
#     if df is not None:
#         for col in df:
#             known = False
#             for data_type in funcs_and_types.keys():
#                 if funcs_and_types[data_type](df[col]):
#                     types.append(data_type)
#                     known = True
#                     break
#             if not known:
#                 types.append(UNKNOWN)
#
#     return types