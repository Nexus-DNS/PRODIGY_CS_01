def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts text using Caesar Cipher algorithm.

  Args:
      text: The text to be encrypted or decrypted.
      shift: The number of positions to shift letters.
      mode: "encrypt" or "decrypt"

  Returns:
      The encrypted or decrypted text.
  """
  result = ""
  for char in text:
    # Check for punctuation and spaces
    if not char.isalpha():
      result += char
      continue
    
    # Convert char to uppercase for easier handling
    char = char.upper()
    
    # Get the ASCII value
    new_ascii = ord(char) + shift

    # Handle wrapping around the alphabet
    if mode == "encrypt":
      new_ascii = (new_ascii - 65) % 26 + 65
    else:
      new_ascii = (new_ascii - 91) % 26 + 91

    # Convert back to character
    result += chr(new_ascii)
  return result

def main():
  # Get user input
  text = input("Enter your message: ")
  shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
  mode = input("Enter 'encrypt' or 'decrypt': ").lower()

  # Check for valid mode
  if mode not in ("encrypt", "decrypt"):
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
    return

  # Perform encryption or decryption
  new_text = caesar_cipher(text, shift, mode)
  print(f"{mode.title()}d message: {new_text}")

if __name__ == "__main__":
  main()
