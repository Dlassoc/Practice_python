def palindrome(word):
   reversed_word = word[::-1]
   if word == reversed_word:
      print(f"{word} es palindromo ")
   else:
      print(f"{word} NO es palindromo")

palindrome("ola")