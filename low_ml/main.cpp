
#include <iostream>
#include <array>
#include <string>

using namespace std;

static size_t totalAllocated = 0;

// Overriding new operator
void* operator new(size_t size) {
    totalAllocated += size; 
    return std::malloc(size);
}

// Overriding delete operator
void operator delete(void* ptr) noexcept {
    std::free(ptr); // Free memory
}

// Neuron activation threshold
static double threshold = 1.5;

// Perceptron unit
struct Perceptron {
    std::array<double, 5> inputs;
    std::array<double, 5> weights;
};

double calculate(Perceptron &perceptron) {
    double sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += perceptron.inputs[i] * perceptron.weights[i];
    }
    return sum;
}

bool activation_relu(double neuron_output) {
    return neuron_output > threshold;
}

int main() {
    std::array<double, 5> inputs = {2, 3, 4, 5, 6};
    std::array<double, 5> weights = {0.1, 0.3, 0.01, -0.8, 0.9};

    Perceptron neuron;

    // Move inputs and weights into the perceptron
    neuron.inputs = std::move(inputs);
    neuron.weights = std::move(weights);

    double neuron_output = calculate(neuron);

    cout << "Neuron output: " << neuron_output 
         << "\nActivation status of neuron: " << activation_relu(neuron_output) << "\n";

    // ========================== Language features =====================================
    int* age = new int();
    cout << "Enter your age: ";
    cin >> *age;
    string people_type = (*age < 20) ? "young" : "old";

    cout << "People type: " << people_type << "\n";

    int num_list[] = {4, 13, 3, 4, 5, 6, 7};

    for (int i : num_list) {
        cout << i << "\n";
    }

    char name[] = {'H', 'A', 'L', 'O', 'N'};

    for (char c : name) {
        cout << c << "-";
    }
    cout << "\n";

    int n = 10;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cout << "Number: " << i << "\n";
        if (i == n / 2) {
            goto jump;
        }
        sum += i;
    }

jump:
    int average = sum / n;
    cout << "Average: " << average << "\n";
    cout << "Total memory allocated: " << totalAllocated << " bytes\n";

    return 0;
}

