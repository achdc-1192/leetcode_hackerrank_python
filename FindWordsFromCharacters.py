#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from collections import OrderedDict
from collections import defaultdict

#words = ["cat","bt","hat","tree"]
#chars = "efg"

#words = ["hello","world","leetcode"]
#chars = "welldonehoneyr"

class Solution:
	def countCharacters(self, words: List[str], chars: str) -> int:
		d = defaultdict(int)
		for char in chars:
			d[char] += 1
		d = OrderedDict(sorted(d.items()))

		ans = 0
		for word in range(len(words)):
			d_new = defaultdict(int)
			for char in range(len(words[word])):
				d_new[words[word][char]] += 1
			d_new = OrderedDict(sorted(d_new.items()))
			res = 0
			for key,value in d_new.items():
				if key not in d.keys():
					res = 0
					break
				elif d_new[key] > d[key]:
					res = 0
					break
				elif d_new[key] <= d[key]:
					res += d_new[key]
			ans += res
		return ans
