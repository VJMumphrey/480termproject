# Get test info used to compare results


# Start of the Reasearch Paper

# parent class for all sections in a paper
# this should encapsulate set of N
class sectionData:
    def __init__(self, sectionData):
        self.sectionData = sectionData

    def getSectionData(self, sectionData):
        return sectionData

    def setSectionData(self, sectionData):
        self.sectionData = sectionData


# P_p
class preliminary_parts(sectionData):
    def __init__(self, sectionData):
        super().__init__(sectionData)


# P_c
class chapter_parts(sectionData):

    def __init__(self, sectionData):
        self.sectionData = []
        super().__init__(sectionData)


# P_a
class appendix_parts(sectionData):
    def __init__(self, sectionData):
        self.sectionData = []
        super().__init__(sectionData)


# P_r
class reference_parts(sectionData):
    def __init__(self, sectionData):
        super().__init__(sectionData)


# parent class for all tokens
# should encapsulate all tokens in t
class tokens:
    def __init__(self, tokenData) -> None:
        self.tokenData = tokenData

    def getTokenData(self, tokenData):
        return tokenData

    def setTokenData(self, tokenData):
        self.tokenData = tokenData
