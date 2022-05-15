from flask import Blueprint, render_template, request

from utils import get_posts_by_content, load_posts_from_json

from config import post_path

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

@main_blueprint.route('/search')
def search_page():
    s = request.args.get("s", "")
    posts = load_posts_from_json(post_path)
    found_posts = get_posts_by_content(posts, s)
    return render_template("post_list.html", found_posts=found_posts, s=s)

