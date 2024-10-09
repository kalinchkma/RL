#include <iostream>
#include <array>
using namespace std;

// neuron activation threshold
static double threshold = 1.5;

// perceptrons unit
struct Perceptron {
    std::array<double, 5> inputs;
    std::array<double, 5> weights;
};

double calculate(Perceptron &perceptron) {
    double sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += perceptron.inputs[i]*perceptron.weights[i];
    }
    return sum;
}


double activation_relu(double neuron_output) {
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

    cout << "Neuron output: " << neuron_output << "\nActivation status of neuron: " << activation_relu(neuron_output) << "\n";
    return 0;
}