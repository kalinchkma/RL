
static THRESH_HOLD: f32 = 0.6;

struct Perceptron {
    inputs: Vec<f32>,
    weights: Vec<f32>
}

fn forward(n: Perceptron) -> Result<f32, String> {
    let mut sum: f32 = 0.0;
    if n.inputs.len() != n.weights.len() {
       return Err("Error inputs and weights dimension not match".to_string());
    }
    for i in 0..n.inputs.len() {
        sum += n.inputs[i] * n.weights[i];
    }
    Ok(sum)
}

fn activation_relu(output: f32) -> bool {
    return THRESH_HOLD > output;
}

pub fn main() {
    let inputs: Vec<f32> = vec![2.0, 3.0, 4.0, 5.0, 6.0];
    let weights: Vec<f32> = vec![-0.9, 0.1, 0.03, -0.9, 0.1];
    
    if let Ok(output) = forward(Perceptron {inputs, weights}) {
        let neuron_output = activation_relu(output);
        println!("Neuront output {}\n After applying activation relu: {}", output, neuron_output as i32);
    } else {
        println!("Error");
    };
     
}




