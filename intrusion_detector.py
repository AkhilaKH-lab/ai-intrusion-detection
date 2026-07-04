# Simple Intrusion Detection System (Beginner Version)

def detect_intrusion(failed_logins, session_duration, unusual_activity):

    if failed_logins > 5:
        return "🚨 Intrusion Detected: Too many failed login attempts"

    if session_duration < 2:
        return "⚠ Suspicious: Very short session"

    if unusual_activity == True:
        return "🚨 Intrusion Detected: Unusual activity detected"

    return "✅ Normal User Activity"


# Test examples
print(detect_intrusion(2, 10, False))
print(detect_intrusion(8, 15, False))
print(detect_intrusion(1, 1, True))
