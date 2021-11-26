import argparse
import norm
import norm_copy

#内積計算
# python Impression2music/main_norm.py music_impression -i 曲名

def music_impression(name):
    word = ["dignified","sad","sentimental","calm","graceful","happy","exciting","vigorous"]
    if name not in word:
        norm_copy.distance(name)
    else:
        norm.distance(name)
    return #name(印象語)を与えると最も近い曲を返す

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

    # このファイル内の関数を取得
    func_dict = {k: v for k, v in locals().items() if callable(v)}
    # 引数のうち，数値として解釈できる要素はfloatにcastする
    func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
    # 関数実行
    ret = func_dict[args.function_name](*func_args)