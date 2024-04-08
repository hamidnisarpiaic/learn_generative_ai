import React from "react";
import { CiSquareCheck } from "react-icons/ci";
import { Todo } from "../../types";
import { FiEdit, FiTrash2 } from "react-icons/fi";
import ToolTip from "../components/ToolTip";
// import { Modal } from "../components/Modal";
import { Modal } from "../components/Modal";

export default function Task({ task }: { task: Todo }) {
  return (
    <tr className="flex justify-between items-center border-b border-gray-300 px-2 py-2">
      <td className="text-gray-800">{task.content}</td>
      <td className="flex gap-x-2">
        <ToolTip tool_tip_content="Mark is completed">
          <CiSquareCheck
            size={28}
            className={`text-${task.is_completed ? "green-500" : "green-700"}`}
          />
        </ToolTip>
        <Modal title="Edit Task" Editing={true}>
        <FiEdit size={24} className={`text-${task.is_completed ? "blue-500" : "blue-700"}`}
        />

        </Modal>
       
        
        <FiTrash2
          size={24}
          className={`text-${task.is_completed ? "red-500" : "red-700"}`}
        />
      </td>
    </tr>
  );
}
