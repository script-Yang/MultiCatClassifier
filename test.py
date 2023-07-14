from tensorflow.keras.models import load_model

# Load the model
model = load_model('model.h5')

# Perform testing
# Assuming you have a test dataset called test_data and corresponding labels called test_labels
loss, accuracy = model.evaluate(test_data, test_labels)

# Print the test results
print('Loss:', loss)
print('Accuracy:', accuracy)
