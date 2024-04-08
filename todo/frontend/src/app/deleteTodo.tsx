import axios from 'axios';
import { useState } from 'react';

const DeleteTodo = () => {
  const [todoId, setTodoId] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.delete(`http://localhost:8000/api/data/${todoId}`);
      console.log('Data deleted:', response.data);
      // Handle success, maybe redirect or show a success message
    } catch (error) {
      console.error('Error deleting data:', error);
      // Handle error, maybe show an error message to the user
    }
  };

  return (
    <div>
      <h1>Delete Data</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Todo ID:
          <input type="text" value={todoId} onChange={e => setTodoId(e.target.value)} />
        </label>
        <button type="submit">Delete</button>
      </form>
    </div>
  );
};

export default DeleteTodo;
