import { Todo } from "../../types";
import Task from "./Task";

export default async function TodoTables() {
    try {
        const response = await fetch('http://127.0.0.1:8000/todos/');
        
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        
        const todoList: Todo[] = await response.json();

        return (
            <table className="w-full">
                <thead>
                    <tr className="flex justify-between items-center px-2 py-1 bg-gray-100 shadow-md">
                        <th>Task</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {todoList.map(task => (
                        <Task key={task.id} task={task} />
                    ))}
                </tbody>
            </table>
        );
    } catch (error) {
        console.error('Fetch failed:', error);
        // Handle the error appropriately, e.g., show an error message to the user
        return <div>Error: Failed to fetch data</div>;
    }
}
