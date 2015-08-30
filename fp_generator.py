import hashlib

class Fp_Generator(object):

	def __init__(self, windowSize, resetPointValue):
		self.windowSize = windowSize
		self.resetPointValue = resetPointValue

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
		return int(inputHash, 16)

	def get_hash(self, inputSeq):
		return hashlib.md5(inputSeq).hexdigest()

if __name__ == '__main__':
	fpGenerator = Fp_Generator(2, 173)
	print fpGenerator.do_generate('abcdef1234')
	print fpGenerator.do_generate('cdcdef1234')
