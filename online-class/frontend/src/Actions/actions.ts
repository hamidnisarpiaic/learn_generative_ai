'use server'

import { json } from "stream/consumers";

// add todo
export async function add_todo(state: { status: string, message: string }, formData: FormData) {
    const new_todo = formData.get('add_task') as string;
    // Add code to handle adding the todo
    try {
        const response = await fetch('https://localhost:8000/todos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // corrected header name to 'Content-Type'
            },
            body: JSON.stringify({ content:new_todo }), // corrected body format
        });

        const data = await response.json();
        return {status:'success', message: 'Todo added successfully'} // assuming you want to return the response data
    } catch (error) {
        console.error('Error adding todo:', error);
        throw error; // rethrow the error or handle it appropriately
    }
}
