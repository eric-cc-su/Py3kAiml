import copy


class InMemorySessionManager():

    _inputHistory = "_inputHistory"     # keys to a queue (list) of recent user input
    _outputHistory = "_outputHistory"   # keys to a queue (list) of recent responses.
    _inputStack = "_inputStack"         # Should always be empty in between calls to respond()

    def __init__(self):
        self._sessions = {}

    def _addSession(self, sessionID):
        if sessionID in self._sessions:
            return
        # Create the session.
        self._sessions[sessionID] = {
            # Initialize the special reserved predicates
            self._inputHistory: [],
            self._outputHistory: [],
            self._inputStack: []
        }

    def _get_session_value(self, sessionID, name):
        return self._sessions[sessionID][name]

    def _set_session_value(self, sessionID, name, value):
        self._sessions[sessionID][name] = value

    def _deleteSession(self, sessionID):
        if sessionID in self._sessions:
            self._sessions.pop(sessionID)

    def getSessionData(self, sessionID = None):
        s = None
        if sessionID is not None:
            try: s = self._sessions[sessionID]
            except KeyError: s = {}
        else:
            s = self._sessions
        return copy.deepcopy(s)