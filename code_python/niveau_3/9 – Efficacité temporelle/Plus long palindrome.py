def longest_palindrome_length(s):
    n = len(s)
    if n == 0:
        return 0

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_length = 0
    for i in range(n):
        # Palindrome de longueur impair centré sur le caractère i
        len1 = expand_around_center(i, i)
        # Palindrome de longueur pair centré entre les caractères i et i+1
        len2 = expand_around_center(i, i + 1)
        # Met à jour la longueur maximale trouvée
        max_length = max(max_length, len1, len2)
    
    return max_length

# Lecture de l'entrée
mot = input().strip()
# Calcul de la longueur du plus long palindrome
print(longest_palindrome_length(mot))