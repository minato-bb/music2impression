import argparse
import create_table
import save_db
import impression
# import normalization

# python add_table.py add_table -i id
def add_table(id):
    create_table.create_music_table()
    
    ids = impression.getTrackIDs('21zv57uvde5x7gw5rqkbs55ty', '{}'.format(id))

    print("get API")
    save_db.save_df(impression.make_df(ids))
    print("save db")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name',
                        type=str,
                        help='set fuction name in this file')
    parser.add_argument('-i', '--func_args',
                        nargs='*',
                        help='args in function',
                        default=[])
    args = parser.parse_args()

    func_dict = {k: v for k, v in locals().items() if callable(v)}

    func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
    
    ret = func_dict[args.function_name](*func_args)