{
 "cells": [
  {
   "cell_type": "code",
   "execution_count":"null",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "********************************\n",
      "Hesap Makinsei Programı\n",
      "\n",
      "işlemler;\n",
      "\n",
      "1. Toplama İşlemi\n",
      "\n",
      "2. Çıkarma İşlemi\n",
      "\n",
      "3. Çarpma İşlemi\n",
      "\n",
      "4. Bölme İşlemi\n",
      "\n",
      "********************************\n",
      "\n",
      "\n",
      "Birinci Sayı:5\n",
      "İkinci Sayı:5\n",
      "işlemi giriniz:3\n",
      "5 ile 5 in çarpımı 25 dir\n"
     ]
    }
   ],
   "source": [
    "# print(\"\"\"********************************\n",
    "# Hesap Makinsei Programı\n",
    "\n",
    "# işlemler;\n",
    "\n",
    "# 1. Toplama İşlemi\n",
    "\n",
    "# 2. Çıkarma İşlemi\n",
    "\n",
    "# 3. Çarpma İşlemi\n",
    "\n",
    "# 4. Bölme İşlemi\n",
    "\n",
    "# ********************************\n",
    "\n",
    "# \"\"\")\n",
    "\n",
    "a = int(input(\"Birinci Sayı:\"))\n",
    "b = int(input(\"İkinci Sayı:\"))\n",
    "\n",
    "işlem = input(\"işlemi giriniz:\")\n",
    "\n",
    "if işlem == \"1\":\n",
    "    print(\"{} ile {} in toplamı {} dir\".format (a,b,a+b))\n",
    "elif işlem == \"2\":\n",
    "    print(\"{} ile {} in farkı {} dir\".format (a,b,a-b))    \n",
    "elif işlem == \"3\":\n",
    "    print(\"{} ile {} in çarpımı {} dir\".format (a,b,a*b))    \n",
    "elif işlem == \"4\":\n",
    "    print(\"{} ile {} nın bölümü {} dir\".format (a,b,a/b))    \n",
    "    \n",
    "else:    \n",
    "    print(\"Geçersiz işlem..........\")\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "null",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "a3be70f8ac964757717ac178d44f47e7ea6e160d7eef1e9ec528577fb40697f9"
  },
  "kernelspec": {
   "display_name": "Python 3.7.1 32-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
