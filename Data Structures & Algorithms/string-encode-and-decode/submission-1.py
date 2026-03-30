class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        'hello' -> 5#hello
        '' -> 0#
        '3#abc' -> 5#3#abc (read first 5 chars after #)
        """
        encoded = []
        
        for s in strs:
            encode = f'{len(s)}#{s}'
            print(f'\tadded {encode}')
            encoded.append(encode)
            
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        while len(s) > 0:
            delim = int(s.find('#'))
            word_length = int(s[0:delim])
            
            # parse next word
            # e.g. '5#hello ...'
            start = delim + 1
            end = start + word_length
            decoded.append(s[start:end])

            # update s
            s = s[end:]
        
        return decoded
