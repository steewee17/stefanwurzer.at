/**
 * WorkflowScene3D.tsx
 * -----------------------------------------------------------------------------
 * React / TypeScript Wrapper für die cineastische 3D-Workflow-Landschaft (Three.js)
 * basierend auf dem n8n-Kernworkflow von Stefan Wurzer.
 * 
 * Verwendbar in Next.js, Vite oder modernen React-Setups.
 * -----------------------------------------------------------------------------
 */

import React, { useEffect, useRef } from 'react';
import { WorkflowScene3D as WorkflowEngine } from './WorkflowScene3D.js';

export interface WorkflowScene3DProps {
  className?: string;
  style?: React.CSSProperties;
  interactive?: boolean;
  showControls?: boolean;
  speed?: number;
  onNodeSelect?: (nodeId: string) => void;
}

export const WorkflowScene3D: React.FC<WorkflowScene3DProps> = ({
  className = '',
  style = {},
  interactive = true,
  showControls = true,
  speed = 1.0,
  onNodeSelect
}) => {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const engineRef = useRef<WorkflowEngine | null>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Instanziere Three.js 3D Engine im isolierten Container
    const engine = new WorkflowEngine({
      container: containerRef.current,
      interactive,
      showControls,
      speed,
      onNodeSelect: (id: string) => {
        if (onNodeSelect) onNodeSelect(id);
      }
    });

    engineRef.current = engine;

    return () => {
      if (engineRef.current) {
        engineRef.current.destroy();
        engineRef.current = null;
      }
    };
  }, [interactive, showControls, speed, onNodeSelect]);

  return (
    <div
      ref={containerRef}
      className={`workflow-scene-3d-container ${className}`}
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        overflow: 'hidden',
        background: '#0A0C10',
        ...style
      }}
    />
  );
};

export default WorkflowScene3D;
