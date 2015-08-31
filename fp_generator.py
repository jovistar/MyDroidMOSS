import hashlib

class Fp_Generator(object):

	def __init__(self, windowSize, resetPointValue):
		self.windowSize = windowSize
		self.resetPointValue = resetPointValue

		self.hashValue = {}
		for x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
			self.hashValue[x] = int(x, 16)

	def do_generate(self, inputSeq):
		finalFp = ''

		piecePoint = 0
		resetPoint = 0
		windowPoint = 0

		rollingHash = ''
		pieceHash = ''

		while True:
			piecePoint = resetPoint
			windowPoint = piecePoint

			if piecePoint >= len(inputSeq):
				break

			while True:
				rollingHash = self.get_hash(inputSeq[windowPoint:windowPoint + self.windowSize])

				if self.cal_hash(rollingHash) >= self.resetPointValue:
					resetPoint = windowPoint + self.windowSize
					pieceHash = self.get_hash(inputSeq[piecePoint:resetPoint])

					finalFp = finalFp + pieceHash
					break
				else:
					windowPoint = windowPoint + 1

					if windowPoint >= len(inputSeq):
						resetPoint = len(inputSeq) + 1
						pieceHash = self.get_hash(inputSeq[piecePoint:resetPoint])

						finalFp = finalFp + pieceHash
						break

		return finalFp

	def cal_hash(self, inputHash):
		inputHashHead = 0
		inputHashTail = len(inputHash)

		hashValue = 0
		while inputHashHead != inputHashTail:
			hashValue = hashValue + self.hashValue[inputHash[inputHashHead]]
			inputHashHead = inputHashHead + 1

		return hashValue

	def get_hash(self, inputSeq):
		return hashlib.md5(inputSeq).hexdigest()

if __name__ == '__main__':
	fpGenerator = Fp_Generator(2, 173)
	print fpGenerator.do_generate('abcdef1234')
	print fpGenerator.do_generate('cdcdef1234')
