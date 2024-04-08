import axios from 'axios';
import { useEffect, useState } from 'react';

interface DataItem {
  id: number;
  name: string;
  // Define other properties as per your data structure
}

const GetData = () => {
  const [data, setData] = useState<DataItem[]>([]);

  useEffect(() => {
    axios.get<DataItem[]>('http://your-fastapi-backend-url/api/data')
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Data</h1>
      <ul>
        {data.map(todo => (
          <li key={todo.id}>{todo.name}</li>
        ))}
        {/* Render other properties as needed */}
      </ul>
    </div>
  );
}

export default GetData;
