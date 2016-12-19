from . import types
PATTERNS = [(types.WHITESPACE, r'\s+'),
            (types.FLOAT, r'(\d*\.){1}\d+\b'),
            (types.INTEGER, r'\d+\b'),
            (types.IDENTIFIER, r'[a-zA-Z]+\d*\b'),
            (types.INTEGERDIVISION, r'//'),
            (types.OTHER, r'[\+\-\*\/\%\^\(\)\,]')] 
