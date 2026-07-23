#isolation testing of history_store.py
#type "python test_history.py" in terminal to run the test

from memory.history_store import load_history, save_history, append_exchange

h = load_history()
append_exchange(h, "user", "hello")
print(h)
save_history(h)