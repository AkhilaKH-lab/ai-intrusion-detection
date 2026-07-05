import hashlib

# In a real system, load this from an environment variable — never hardcode secrets in source control.
SALT = "change_this_to_a_real_secret_in_production"

def pseudonymize(student_id: str) -> str:
    """
    Converts a plain-text student ID into an irreversible pseudonym.
    Same input always produces the same output (so you can still track
    repeat behavior for one student), but the original ID can't be
    recovered from it.
    """
    salted = (SALT + student_id).encode("utf-8")
    return hashlib.sha256(salted).hexdigest()[:16]