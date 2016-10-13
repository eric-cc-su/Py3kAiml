import copy


class InMemorySessionManager():

    _inputHistory = "_inputHistory"     # keys to a queue (list) of recent user input
    _outputHistory = "_outputHistory"   # keys to a queue (list) of recent responses.
    _inputStack = "_inputStack"         # Should always be empty in between calls to respond()

    def _addSession(self, sessionID):
        if not sessionID in self._sessions:
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
        s = self._sessions
        if sessionID and sessionID in self._sessions:
            s = self._sessions[sessionID]

        return copy.deepcopy(s)