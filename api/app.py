
from flask import Flask, request, jsonify
from bots import gmeet, zoom, teams

app = Flask(__name__)

# Endpoint to start recording
@app.route('/startRecording', methods=['POST'])
def start_recording():
    # Get arguments from the request
    meeting_id = request.form.get('meetingID')
    meeting_type = request.form.get('meetingType')
    meeting_link = request.form.get('meetingLink')

    # Check if all required arguments are present
    if not meeting_id or not meeting_type or not meeting_link:
        return jsonify({"error": "Missing one or more required parameters"}), 400

    # Call the appropriate function based on meeting type
    if meeting_type.upper() == 'GMEET':
        gmeet.start_gmeet_recording(meeting_id, meeting_link)
    elif meeting_type.upper() == 'ZOOM':
        zoom.start_zoom_recording(meeting_id, meeting_link)
    elif meeting_type.upper() == 'TEAMS':
        teams.start_teams_recording(meeting_id, meeting_link)
    else:
        return jsonify({"error": "Invalid meeting type"}), 400

    return jsonify({
        "message": "Recording started",
        "meetingID": meeting_id,
        "meetingType": meeting_type,
        "meetingLink": meeting_link
    }), 200

# Test endpoint
@app.route('/test', methods=['GET'])
def test():
    return "Test route is working"

if __name__ == '__main__':
    app.run(debug=True)
