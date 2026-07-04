from router import AIRouter

# Example usage of the autonomous router
router = AIRouter()
print("Starting agentic task verification...")

task = "Generate system audit log for node-01"
result = router.route_request(task)

print(f"Task result: {result}")
