def calculate_even_number(ean13barcode):
  sum_evenNum = 0;
  
  for i in range(1,len(ean13barcode),2):
    sum_evenNum += int(ean13barcode[i]);

  sum_evenNum *= 3;
  return sum_evenNum;

def calculate_odd_number(ean13barcode):
  sum_oddNum = 0;

  for i in range(0, len(ean13barcode)-1, 2):
    sum_oddNum += int(ean13barcode[i]);

  return sum_oddNum;

def check_ean13(ean13barcode):
  even_number = calculate_even_number(ean13barcode);  #1) Sum of the digits in even positions and then multiplied by 3. -> 2, 4, 6, 8, 0, 2 = 22; 22 * 3 = 66;
  odd_number = calculate_odd_number(ean13barcode);    #2) Sum of the digits in odd positions excluding the last digit. ->  1, 3, 5, 7, 9, 1 = 26;
  sumNum = (even_number + odd_number) % 10;           #3) Sum of odd and even and get the remainder of 10. -> 66 + 26 = 92; 92 mod 10 = 2;
  
  if (sumNum == 0):                                   #4.1) If there is no remainder then it's correct. 2 != 0; so go to next check
    return True;
  else:
    if((10-sumNum) == int(ean13barcode[12])):         #4.2) Else 10 minus the module of the last value in ean13barcode needs to be equal to the last digit; is 10 - 2 = 8? Correct.
      return True;
    else:
      return False;

def generate_ean13():
  #1234567890111
  #Format: XXXXX-XXXX-XXXX
  start_barcode = "50000";
  second_part = "6789";
  third_part = "0111";  #Default barcode
  list_of_barcodes = [];

  #Check if there is any file if there isn't start from the default barcode
  try:
    with open('used_barcode.txt', 'r') as f:
      list_of_barcodes = f.read().splitlines(); #remove the \n from the values in list
      ean13barcode = list_of_barcodes[-1];  #Start from the last generated barcode
  except:
    ean13barcode = (start_barcode + second_part + third_part);
    

  #Loop through the increment of the barcode until the formula fits the format.
  while(True):
    flag = check_ean13(str(ean13barcode));
    ean13barcode = int(ean13barcode);
    if(flag == True):
      if str(ean13barcode) not in list_of_barcodes: #if it fits the format, check if it was already previously generated
        f = open("used_barcode.txt", "a");
        f.write(str(ean13barcode)+"\n");
        f.close();
        break;
      else:
        ean13barcode+=1;  #if it exists in the file isn't go to the next
    else:
      ean13barcode+=1;    #if it doesn't fit the formula check next

  return ean13barcode;

if __name__ == "__main__":
  t = generate_ean13();
  print(t);