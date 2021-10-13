'''

NAME: HARSH SINGHANIA 
HW03- FRACTION
CWID- 20007289
Creating a python code for Fraction Calculator. Defining different classes for different operations to be performed in this program.
Using if/else to determine which operation needs to be implemented and a while loop to ask the user to re-enter the values if any invalid input is given.

'''

from fractions import Fraction
class Fraction:
    """Fraction class"""
    def __init__(self,numerator,denominator) -> None:
        """Creating init function for accepting numerator and denominator. Returning value error if denominator is entered 0."""
        self.numerator: int = numerator
        self.denominator: int = denominator
            
    def __add__(self, other) ->"Fraction":
        """Creating a function to perform fraction addition operation."""
        return Fraction( ((self.numerator * other.denominator) + (other.numerator * self.denominator)),self.denominator * other.denominator) 

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Creating a function to perform fraction subtraction operation."""
        den: int = self.denominator * other.denominator
        num: int = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Fraction(num,den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Creating a function to perform fraction multiplication operation."""
        den: int = self.denominator * other.denominator
        num: int = self.numerator * other.numerator
        return Fraction(num,den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Creating a function to perform fraction division operation."""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other: "Fraction") -> bool:
        """Creating a function to check whether both the self and other fraction is equal."""
        if ((self.numerator*other.denominator) == (self.denominator*other.numerator)):
            return True
        else:
            return False
    
    def __ne__(self, other: "Fraction") -> bool:
        """Creating a function to check whether both the self and other fraction is not equal."""
        if self.numerator * other.denominator != self.denominator * other.numerator:
            return True
        else:
            return False

    def __lt__(self, other:"Fraction") -> bool:
        """Creating a function to compare Less Than condition of 2 Fractions."""
        if self.numerator * other.denominator < self.denominator * other.numerator:
            return True
        else:
            return False

    def __le__(self, other:"Fraction") -> bool:
        """Creating a function to compare Less Than or Equal to condition of 2 Fractions."""
        if self.numerator * other.denominator <= self.denominator * other.numerator:
            return True
        else:
            return False

    def __gt__(self, other:"Fraction") -> bool:
        """Creating a function to compare Greater Than condition of 2 Fractions."""
        if self.numerator * other.denominator > self.denominator * other.numerator:
            return True
        else:
            return False

    def __ge__(self, other: "Fraction") -> bool:
        """Creating a function to compare Greater Than or Equal to condition of 2 Fractions."""
        if self.numerator * other.denominator >= self.denominator * other.numerator:
            return True
        else:
            return False

    def __str__(self) -> str:
        """Returning string representation of the fraction."""
        return f"{self.numerator} / {self.denominator}"
        

def main() -> None:
    print("Hello! Welcome to the Fraction Calculator.\n")

    while True:
        """Taking input of numerator and denominator of both the fractions from the user and the operator as well. Mapping the respective operator to the 
        operation that needs to be performed using if/else statements."""

        numerator = int(input("Enter the 1st fraction numerator:"))
        try:
            denominator = int(input("\nEnter the 1st fraction denominator:"))
            Frac1 = Fraction(numerator,denominator)
            if denominator ==0:
                raise ZeroDivisionError("Please enter non-zero integer only. \n")
        except ZeroDivisionError as z:
            print (z)
            continue

        op: str = input("\nEnter the operation to be performed: ( +, -, /, *, ==, !=, <, <=, >, >= ) ")
        
        if (op == "+" or "-" or "*" or "/" or "==" or "!=" or "<" or ">" or "<=" or ">="):
            numerator = int(input("\nEnter the 2nd fraction numerator:"))
            try:
                denominator = int(input("\nEnter the 1st fraction denominator:"))
                Frac2 = Fraction(numerator,denominator)
                if denominator ==0:
                    raise ValueError("Please enter a non zero inetger.\n")
            except ValueError as e:
                print(e)
                continue

            if op == "+":
                result: Fraction = Frac1 + Frac2
                print(Frac1," + ",Frac2," = ",result)
                break

            elif op == "-":
                result: Fraction = Frac1 - Frac2
                print(Frac1," - ",Frac2," = ",result)
                break

            elif op == "/":
                result: Fraction = Frac1 / Frac2
                print(Frac1," / ",Frac2," = ",result)
                break

            elif op == "*":
                result: Fraction = Frac1 * Frac2
                print(Frac1," * ",Frac2," = ",result)
                break

            elif op == "==":
                result: Fraction = (Frac1 == Frac2)
                print(result)
                break

            elif op == "!=":
                result: Fraction = Frac1 != Frac2
                print(result)
                break
            
            elif op == "<":
                result: Fraction = Frac1 < Frac2
                print(result)
                break
            
            elif op == "<=":
                result: Fraction = Frac1 <= Frac2
                print(result)
                break

            elif op == ">":
                result: Fraction = Frac1 > Frac2
                print(result)
                break

            elif op == ">=":
                result: Fraction = Frac1 >= Frac2
                print(result)
                break

            else:
                print("INVALID, PLease enter operator from the options provided")

if __name__ == '__main__':
    main()
    