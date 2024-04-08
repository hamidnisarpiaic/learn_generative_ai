import React from "react";
import { Button } from "./ui/button"; // Corrected path and corrected capitalization
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "./ui/tooltip"; // Corrected capitalization

export default function ToolTip({ tool_tip_content, children }: { tool_tip_content: string; children: React.ReactNode }) {
  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          {children}
        </TooltipTrigger>
        <TooltipContent>
          <p>{tool_tip_content}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}
