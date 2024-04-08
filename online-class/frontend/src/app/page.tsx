import { Modal } from "../components/Modal";
import TodoTables from "@/components/TodoTables";
import { Button } from "@/components/ui/button";
import Image from "next/image";

export default function Home() {
  return (
    <main className="max-w-5xl mx-auto pt-8">
   {/* Add Sections */}
<section>
<Modal title="Add New Task" Adding={true}>
<Button variant="default" className="w-full bg-teal-600 hover:bg-teal-700 px-4 py-2 text-lg uppercase text-white">
  Add Task
</Button>

</Modal>
</section>
{/* Todo Table */}

<section className="mt-4">
  <TodoTables/>
</section>



    </main>
  );
}
