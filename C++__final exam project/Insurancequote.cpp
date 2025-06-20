#include <iostream>
#include <cstring>
using namespace std;

// Structure to store applicant information
struct Applicant {
    char vin[17];
    int age;
    char vehicleType[10];
};

// Structure to store rate bracket information
struct RateBracket {
    float minAge;
    float maxAge;
    float premium;
};

// Abstract base class for insurance quote engines
class QuoteEngine {
protected:
    RateBracket* brackets; // Dynamic array of brackets
    int count;             // Number of brackets

public:
    QuoteEngine() {
        brackets = nullptr;
        count = 0;
    }

    // Virtual function to compute quote
    virtual float getQuote(const Applicant* applicant) = 0;

    // Add a rate bracket
    void addBracket(RateBracket newBracket) {
        RateBracket* temp = new RateBracket[count + 1];
        for (int i = 0; i < count; i++) {
            *(temp + i) = *(brackets + i); // pointer arithmetic
        }
        *(temp + count) = newBracket;
        delete[] brackets;
        brackets = temp;
        count++;
    }

    // Remove a rate bracket by index
    void removeBracket(int index) {
        if (index < 0 || index >= count) return;
        RateBracket* temp = new RateBracket[count - 1];
        for (int i = 0, j = 0; i < count; i++) {
            if (i != index) {
                *(temp + j) = *(brackets + i);
                j++;
            }
        }
        delete[] brackets;
        brackets = temp;
        count--;
    }

    // Destructor
    virtual ~QuoteEngine() {
        delete[] brackets;
    }
};

// Basic quote engine (uses regular premium)
class BasicEngine : public QuoteEngine {
public:
    float getQuote(const Applicant* applicant) {
        for (int i = 0; i < count; i++) {
            RateBracket* rb = brackets + i; // pointer arithmetic
            if (applicant->age >= rb->minAge && applicant->age <= rb->maxAge) {
                return rb->premium;
            }
        }
        return 0.0;
    }
};

// Premium quote engine (adds a markup)
class PremiumEngine : public QuoteEngine {
public:
    float getQuote(const Applicant* applicant) {
        for (int i = 0; i < count; i++) {
            RateBracket* rb = brackets + i;
            if (applicant->age >= rb->minAge && applicant->age <= rb->maxAge) {
                return rb->premium * 1.5f;
            }
        }
        return 0.0;
    }
};

// Main function
int main() {
    // Create sample applicant
    Applicant a;
    strcpy(a.vin, "RW123456789012345");
    a.age = 30;
    strcpy(a.vehicleType, "car");

    // Create dynamic array of quote engines
    QuoteEngine** engines = new QuoteEngine*[2];
    engines[0] = new BasicEngine();
    engines[1] = new PremiumEngine();

    // Define rate brackets
    RateBracket b1 = {18, 25, 120.0};
    RateBracket b2 = {26, 35, 100.0};
    RateBracket b3 = {36, 60, 90.0};

    // Add brackets to engines
    for (int i = 0; i < 2; i++) {
        engines[i]->addBracket(b1);
        engines[i]->addBracket(b2);
        engines[i]->addBracket(b3);
    }

    // Show quotes from each engine
    for (int i = 0; i < 2; i++) {
        float quote = engines[i]->getQuote(&a);
        cout << "Engine " << (i == 0 ? "Basic" : "Premium") << " Quote: $" << quote << endl;
    }

    // Free memory
    for (int i = 0; i < 2; i++) {
        delete engines[i];
    }
    delete[] engines;

    return 0;
}

