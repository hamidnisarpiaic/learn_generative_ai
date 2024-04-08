'use client'
import React from "react";
import { useFormState } from "react-dom"; // Corrected import statement

import { add_todo } from "@/Actions/actions";

export default function AddTask() { // Changed to export default function
  const [state, formAction] = useFormState(add_todo, { status: "", message: "" }); // Corrected syntax
  const { status, message } = state; // Destructured state objec to extract status and message

  return (
    <div>
      <form action={formAction} className="flex flex-col justify-between items-center gap-x-3 w-full">
        <input
          type="text"
          placeholder="Add Task here"
          minLength={3}
          maxLength={54}
          required
          name="add_task"
          className="w-full px-3 py-2 border border-gray-100 rounded-md"
        />
        <button type="submit" className="px-2 py-1 bg-teal-600 text-white rounded-md w-full mt-4">Save</button>
      </form>
    </div>
  );
}
