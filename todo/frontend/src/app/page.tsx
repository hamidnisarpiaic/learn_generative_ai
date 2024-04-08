"use client"
import AddTodo from '@/app/addTodo';
import DeleteTodo from '@/app/deleteTodo';
import UpdateTodo from '@/app/updateTodo';
import GetTodo from '@/app/getData';
import PostData from '@/app/postTodo';

const Page = () => {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-4xl font-bold mb-8 text-center">To Do Management</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-blue-100 p-6 rounded-lg shadow-md">
          
          <div className="mb-4">
            <input type="text" placeholder="Enter todo" className="border rounded-lg p-2 w-full" />
          </div>
          <AddTodo />
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4">
            Post
          </button>
        </div>
        <div className="bg-green-100 p-6 rounded-lg shadow-md">
         
          <DeleteTodo />
          <button className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mt-4">
            Delete
          </button>
        </div>
        <div className="bg-yellow-100 p-6 rounded-lg shadow-md">
          
          <UpdateTodo />
          <button className="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded mt-4">
            Update
          </button>
        </div>
        <div className="bg-pink-100 p-6 rounded-lg shadow-md">
          
          <GetTodo />
        </div>
      </div>
    </div>
  );
};

export default Page;
