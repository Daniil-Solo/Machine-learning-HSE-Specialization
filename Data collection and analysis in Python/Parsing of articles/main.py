from Parser import ArticleParser
import argparse

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--parsing_type', dest='parsing_type', type=str, default='last 10',
                            help='Example: last 4, first 10, all')
    arg_parser.add_argument('--user_agent', dest='user_agent', type=str, default=None, help='No help')
    arg_parser.add_argument('--path', dest='path', type=str, default='article_data.csv', help='No help')

    args = arg_parser.parse_args()
    parsing_type = args.parsing_type
    user_agent = args.user_agent
    path = args.path

    article_parser = ArticleParser(user_agent=user_agent)
    article_parser.start(parsing_type=parsing_type)
    article_parser.save_table(path=path)
