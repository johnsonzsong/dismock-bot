'''
	Run with:
		python example_tests.py TARGET_NAME TESTER_TOKEN
		botty MTA4NDY4NjY1MDcwMzA4NTY4MA.GzlNPK.LybpCjqxdn8SKVTnyl1SwhYeMEQP6QUFN20MB4
'''

import sys
import dismock

# The tests themselves

testcollector = dismock.TestCollector()

@testcollector()
async def test_ping(interface):
	await interface.assert_reply_equals('ping?', 'pong!')

@testcollector()
async def test_new_one(interface):
	await interface.assert_reply_equals('hello', 'world!')

# Make it easy to run the tests

if __name__ == '__main__':
	_, target_name, token = sys.argv
	dismock.run_interactive_bot(target_name, token, testcollector)
