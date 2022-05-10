from flask import Blueprint, render_template, request


from config import post_path
from utils import load_posts_from_json, upload_posts_to_json

# import logging
#
# logger = logging.getLogger("basic")
# logger.setLevel("DEBUG")
#
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
#
# file_handler = logging.FileHandler("logs/basic.txt")
# logger.addHandler(file_handler)
#
# file_handler_2 = logging.FileHandler("logs/basic_2.txt")
# logger.addHandler(file_handler_2)
#
# formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s  %(pathname)s >> %(funcName)s")
# stream_handler.setFormatter(formatter)


loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix="/post", static_folder="/static/css", template_folder="templates")

@loader_blueprint.route('/form/')
def main_page():
    return render_template("post_form.html")

@loader_blueprint.route('/uploads/', methods=["POST"])
def upload_page():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_posts_from_json(post_path)
        posts.append({'pic': f'/uploads/images/{filename}', 'content': content})
        upload_posts_to_json(posts)
        file.save(f'uploads/{filename}')
    except FileNotFoundError:
        return "<h1>Файл не найден</h1>"

    else:
        return render_template("post_uploaded.html", pic=f'/uploads/images/{filename}', content=content)


# print(post_path)
# @main_blueprint.route('/search')
# def search_page():
#     s = request.args.get("s", "")
#     # posts = load_posts_from_json(POST_PATH)
#     found_posts = get_posts_by_content(POST_PATH, s)
#     return render_template("post_list.html", found_posts=found_posts, s=s)
