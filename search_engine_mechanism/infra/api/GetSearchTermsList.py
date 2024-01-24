from flask import Flask, request, jsonify
from search_engine_mechanism.infra.SearchTermsOption import SearchTermsOption

app = Flask(__name__)
database_path = "example.db"  # Replace with your actual database path
search_terms_option = SearchTermsOption(database_path)


@app.route('/search', methods=['GET'])
def search_terms():
    try:
        search_term = request.args.get('search_term')

        if not search_term:
            return jsonify({"status": "error", "data": [], "msg": "Search term is missing"}), 400

        search_results = search_terms_option.getSearchTermOptions(search_term)

        if search_results:
            response_data = [{"option_value": result['option_value'], "product_page_url": result['product_page_url']}
                             for result in search_results]
            return jsonify({"status": "success", "data": response_data})
        else:
            return jsonify({"status": "success", "data": [], "msg": "No Data Found"})
    except Exception as e:
        return jsonify({"status": "error", "data": [], "msg": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
