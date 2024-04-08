import axios from 'axios';
import { useState } from 'react';

const UpdateTodo = () => {
  const [todoId, setTodoId] = useState('');
  const [updatedData, setUpdatedData] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.put(`http://localhost:8000/api/data/${todoId}`, { updatedData });
      console.log('Data updated:', response.data);
      // Handle success, maybe redirect or show a success message
    } catch (error) {
      console.error('Error updating data:', error);
      // Handle error, maybe show an error message to the user
    }
  };

  return (
    <div>
      <h1>Update Data</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Item ID:
          <input type="text" value={todoId} onChange={e => setTodoId(e.target.value)} />
        </label>
        <label>
          Updated Data:
          <input type="text" value={updatedData} onChange={e => setUpdatedData(e.target.value)} />
        </label>
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default UpdateTodo;
