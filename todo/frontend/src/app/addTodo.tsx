import axios from 'axios';
import { useState } from 'react';

const AddTodo = () => {
  const [formData, setFormData] = useState({
    // Define your form fields here
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/data', formData);
      console.log('Data added:', response.data);
      // Handle success, maybe redirect or show a success message
    } catch (error) {
      console.error('Error adding data:', error);
      // Handle error, maybe show an error message to the user
    }
  };

  return (
    <div>
      <h1>Add Todo</h1>
      <form onSubmit={handleSubmit}>
        {/* Render your form inputs here */}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddTodo;
