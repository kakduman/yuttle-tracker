import load_dataset as ld
import numpy as np

def calculate_metrics(estimated_times, arrivals):
    '''
    Compute the Mean Absolute Error (MAE) and Mean Squared Error (MSE) between estimated and actual arrival times.

    Args:
        estimated_times (dict): A dictionary of estimated arrival times for each stop.
        arrivals (dict): A dictionary of actual arrival times for each stop.

    Returns:
        tuple: A tuple containing the MAE and MSE between estimated and actual arrival times.

    '''

    # Find common stops between estimatedTimes and arrivals
    common_stops = set(estimated_times.keys()) & set(arrivals.keys())
    if not common_stops:
        return None, None
    
    # Calculate the differences between estimated and actual arrival times
    try:
        differences = [arrivals[stop] - estimated_times[stop] for stop in common_stops]
    except:
        return None, None
    
    # Calculate Mean Absolute Error (MAE)
    mae = np.mean(np.abs(differences))
    
    # Calculate Mean Squared Error (MSE)
    mse = np.mean(np.square(differences))
    
    return mae, mse


def calculate_mae(predictions, ground_truth):
    '''
    Calculate the Mean Absolute Error (MAE) between predicted and ground truth values.

    Args:
        predictions (list): A list of predicted values.
        ground_truth (list): A list of ground truth values.

    Returns:
        float: The Mean Absolute Error (MAE) between predicted and ground truth values.

    '''
    return np.mean(np.abs(np.array(predictions) - np.array(ground_truth)))

def calculate_mae_data(predicted_times, true_arrivals):
    '''
    Calculate the Mean Absolute Error (MAE) between predicted and true arrival times.

    Args:
        predicted_times (dict): A dictionary of predicted arrival times for each stop.
        true_arrivals (dict): A dictionary of true arrival times for each stop.

    Returns:
        float: The Mean Absolute Error (MAE) between predicted and true arrival times.

    '''
    mae, mse = calculate_metrics(predicted_times, true_arrivals)
    return mae

if __name__ == '__main__':
    dataset = ld.load_estimate_dataset()

    # Make a test dataset of the first 10 entries
    # dataset = dataset[:10]

    metrics = [calculate_metrics(pair[0], pair[1]) for pair in dataset if pair[0] and pair[1]]
    valid_metrics = [m for m in metrics if m[0] is not None and m[1] is not None]
    if valid_metrics:
        avg_mae = np.mean([m[0] for m in valid_metrics])
        avg_mse = np.mean([m[1] for m in valid_metrics])
        print(f"Average MAE: {avg_mae:.4f}")
        print(f"Average MSE: {avg_mse:.4f}")
    else:
        print("No valid metrics found.")