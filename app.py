from flask import Flask, request, jsonify
from jobspy import scrape_jobs

app = Flask(__name__)

@app.route('/scrape_jobs', methods=['POST'])
def scrape_jobs_api():
    try:
        data = request.get_json()

        site_name = data.get('site_name', [])
        search_term = data.get('search_term', 'software engineer')
        location = data.get('location', 'Dallas, TX')
        results_wanted = data.get('results_wanted', 50)
        country_indeed = data.get('country_indeed', 'USA')
        offset = data.get('offset', 25)

        jobs = scrape_jobs(
            site_name=site_name,
            search_term=search_term,
            location=location,
            results_wanted=results_wanted,
            country_indeed=country_indeed,
            offset=offset
        )
        
        # If you want to return JSON response
        return jsonify(jobs.to_dict(orient='records'))

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400  # Return the error and set HTTP status code to 400

if __name__ == '__main__':
    app.run()
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
