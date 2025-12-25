import { defineStore } from 'pinia'

export interface LogAnalysisEntry {
  ip: string // The attacker's IP
  count: number // Number of failed attempts
  users: string[] // List of usernames they tried to use
}

export const useLogStore = defineStore('logStore', {
  state: () => ({
    status: 'idle' as 'idle' | 'uploading' | 'success' | 'error',
    errorMessage: '',
    selectedFileName: '',
    analysisResults: [] as LogAnalysisEntry[], // To store the IP data
  }),

  actions: {
    async handleFileUpload(file: File) {
      this.status = 'uploading';
      this.errorMessage = '';
      this.selectedFileName = file.name;

      // Prepare the data for transport
      const formData = new FormData()
      formData.append('file', file)

      const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
      
      try {
        const response = await fetch(`${API_BASE_URL}/analyze`, {
          method: 'POST',
          body: formData,
        })

        if (!response.ok) throw new Error('Backend error')

        const data = await response.json()
        this.analysisResults = data.results
        this.status = 'success'
      } catch (error: unknown) {
        this.status = 'error'
        this.errorMessage = error instanceof Error ? error.message : 'Failed to connect to backend.'
      }
    },

    resetState() {
      this.status = 'idle';
      this.analysisResults = [];
      this.errorMessage = '';
      this.selectedFileName = '';
    },
  },
})
