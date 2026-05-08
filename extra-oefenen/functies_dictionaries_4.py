def update_status(task, nieuwe_status):
    task["status"] = nieuwe_status
    return task


taak = {
    "titel": "Week 9 Python oefenen",
    "status": "open"
}

print("Voor update:", taak)

taak = update_status(taak, "afgerond")

print("Na update:", taak)
