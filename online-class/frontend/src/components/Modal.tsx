import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import Addtask from "@/components/AddTask";
import EditTask from "@/components/EditTask"
import { ReactNode } from "react";

export function Modal({children, title, Adding, Editing}:{children:React.ReactNode, title:string, Adding?:boolean, Editing?:boolean}) {
  return (
    <Dialog>
      <DialogTrigger asChild>
        {children}
       
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>{title}</DialogTitle>
        </DialogHeader>
        {Adding && <Addtask/>}
        {Editing && <EditTask/>}
      </DialogContent>
    </Dialog>
  );
}
